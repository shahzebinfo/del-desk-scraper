import dotenv from "dotenv";
dotenv.config();

import { scrapeData } from "./services/scraperService.js";
import { updateSheet } from "./services/sheetsService.js";

async function runTask() {
  console.log("🚀 Running scrape + sheet update task...");
  const data = await scrapeData();
  await updateSheet(data);
}

runTask();
setInterval(runTask, 5 * 60 * 1000); // repeat every 5 minutes
