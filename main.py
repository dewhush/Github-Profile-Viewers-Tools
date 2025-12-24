import time
import random
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Cache the driver path once to avoid repeated calls to manager
DRIVER_PATH = None

class GitHubProfileVisitor:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless=new")
        
        # Anti-detection settings / Optimization
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.page_load_strategy = 'eager' # Don't wait for full load
        
        # User agent
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Use cached driver path
        global DRIVER_PATH
        if DRIVER_PATH is None:
            DRIVER_PATH = ChromeDriverManager().install()
            
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH), options=self.chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    def human_like_scroll(self):
        """Faster scroll simulation"""
        try:
            scroll_amounts = [random.randint(300, 700) for _ in range(2)] # Reduced scroll count
            for amount in scroll_amounts:
                self.driver.execute_script(f"window.scrollBy(0, {amount});")
                time.sleep(random.uniform(0.1, 0.3)) # Faster scroll delay
        except:
            pass
    
    def visit_profile(self, username):
        """Visit GitHub profile with reduced delays"""
        url = f"https://github.com/{username}"
        
        try:
            # Navigate to profile
            self.driver.get(url)
            
            # Wait for key element (reduced timeout)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Very short interaction
            self.human_like_scroll()
            time.sleep(random.uniform(0.5, 1.5)) # Reduced visit time
            
            return True
            
        except Exception as e:
            logger.error(f"Error visiting {username}: {str(e)}")
            return False
    
    def cleanup(self):
        """Close browser"""
        try:
            self.driver.quit()
        except:
            pass

def run_visit(target_username, visit_id, total_visits):
    visitor = None
    try:
        visitor = GitHubProfileVisitor()
        success = visitor.visit_profile(target_username)
        if success:
            logger.info(f"[+] Visit {visit_id}/{total_visits} success")
        else:
            logger.info(f"[-] Visit {visit_id}/{total_visits} failed")
        return success
    except Exception as e:
        logger.error(f"Error in thread {visit_id}: {e}")
        return False
    finally:
        if visitor:
            visitor.cleanup()

def main():
    global DRIVER_PATH
    try:
        logger.info("Initializing... Pre-loading driver.")
        DRIVER_PATH = ChromeDriverManager().install()
        
        print("\n=== GitHub Profile Viewer (Fast Mode) ===")
        target_username = input("Target Username: ").strip()
        if not target_username:
            print("Username cannot be empty.")
            return

        visit_count_input = input("Number of Views: ").strip()
        if not visit_count_input.isdigit():
            print("Invalid number.")
            return
        visit_count = int(visit_count_input)
        
        workers_input = input("Number of Threads (Default 5): ").strip()
        max_workers = int(workers_input) if workers_input.isdigit() else 5
        
        logger.info(f"Target: @{target_username} | Visits: {visit_count} | Threads: {max_workers}")
        
        successful_visits = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(run_visit, target_username, i+1, visit_count) for i in range(visit_count)]
            
            for future in as_completed(futures):
                if future.result():
                    successful_visits += 1
        
        logger.info(f"Done! {successful_visits}/{visit_count} successful.")
            
    except KeyboardInterrupt:
        print("\n[INFO] Program stopped by user.")
    except Exception as e:
        logger.error(f"Fatal error: {e}")

if __name__ == "__main__":
    main()