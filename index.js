import dotenv from 'dotenv';
dotenv.config();

import { getSheetData } from './services/sheetsService.js';

async function main() {
  try {
    const data = await getSheetData(process.env.GOOGLE_SHEET_ID, 'Sheet1!A1:D10');
    console.log('Data from Google Sheet:');
    console.table(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

main();
