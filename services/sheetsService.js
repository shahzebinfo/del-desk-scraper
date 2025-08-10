import { google } from 'googleapis';
import fs from 'fs';

export async function getSheetData(sheetId, range) {
  const credentials = JSON.parse(fs.readFileSync(process.env.GOOGLE_CREDENTIALS, 'utf8'));

  const auth = new google.auth.GoogleAuth({
    credentials,
    scopes: ['https://www.googleapis.com/auth/spreadsheets.readonly'],
  });

  const sheets = google.sheets({ version: 'v4', auth });

  const res = await sheets.spreadsheets.values.get({
    spreadsheetId: sheetId,
    range: range,
  });

  return res.data.values || [];
}
