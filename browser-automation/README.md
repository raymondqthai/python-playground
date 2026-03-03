# Browser Automation with Selenium

A Python script that automates Google Chrome to search Startpage.com and click a specific search result. Built as a learning project to practice browser automation, element selection, and dynamic page interaction using Selenium.

---

## Features

- Launches a Chrome browser window automatically
- Navigates to Startpage.com and submits a search query
- Waits for page elements to load before interacting with them
- Clicks a target link from the search results
- Closes the browser after a short delay

---

## Requirements

You need Python installed. Then install Selenium:

```
pip3 install selenium
```

Selenium on Mac automatically downloads the correct ChromeDriver for you. No manual setup needed.

**Windows users:** You need to download ChromeDriver manually and update the script to use the `Service` path. Instructions are in the comments inside `browser_automation.py`.

---

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/yourusername/your-repo.git
   ```
2. Navigate to the folder
   ```
   cd your-repo
   ```
3. Run the script
   ```
   python3 browser_automation.py
   ```

A Chrome window will open, search Startpage.com, and click the first matching result. The browser closes after 10 seconds.

---

## No API Key Required

This tool works out of the box. You do not need to register for any service or set up API credentials.

---

## Usage

When you run the script, Chrome opens and performs these steps automatically:

```
1. Opens https://www.startpage.com
2. Types: "linkedin raymond-thai-9552bb87"
3. Presses Enter
4. Waits for results to load
5. Finds and clicks the "Raymond Thai" link
6. Waits 10 seconds
7. Closes the browser
```

To search for something different, edit this line in `browser_automation.py`:

```python
input_element.send_keys("linkedin raymond-thai-9552bb87" + Keys.ENTER)
```

Replace the search text with your own query.

---

## What I Learned

- How to set up Selenium and control a Chrome browser with Python
- How to locate HTML elements using class names and partial link text
- How to use `WebDriverWait` to pause execution until a page element appears
- How to send keyboard input and click links through the browser driver
- How Mac handles ChromeDriver automatically, and why Windows requires a manual path

---

## Credits

Based on a tutorial by Tech With Tim.
Link: https://www.youtube.com/watch?v=NB8OceGZGjA&t=101s

Some code was adjusted to work on macOS and a different IDE.
