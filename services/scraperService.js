import { Builder, By, until } from "selenium-webdriver";
import chrome from "selenium-webdriver/chrome.js";

export async function scrapeData() {
  const options = new chrome.Options();
  options.addArguments(
    '--headless=new',            // latest headless mode
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--window-size=1920,1080'
  );

  // Chrome binary path set karo (Railway/Docker ke liye)
  options.setChromeBinaryPath(process.env.CHROME_BIN || '/usr/bin/chromium');

  let driver = await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();

  try {
    await driver.get("https://del-desk.excitel.in/tickets/advancedSearch/1?listData=%7B%22sortBy%22:%7B%7D,%22currentPage%22:1,%22timestamp%22:1754761622480%7D");

    await driver.findElement(By.name("username")).sendKeys(process.env.EXCITEL_USER);
    await driver.findElement(By.name("password")).sendKeys(process.env.EXCITEL_PASS);
    await driver.findElement(By.css("button[type='submit']")).click();

    await driver.wait(until.elementLocated(By.tagName("body")), 10000);

    const pageText = await driver.findElement(By.tagName("body")).getText();
    const lines = pageText.split("\n");

    return lines;
  } finally {
    await driver.quit();
  }
}
