import { google } from "googleapis";

export async function updateSheet(values) {
  const creds = JSON.parse(process.env.GOOGLE_CREDENTIALS);

  const client = new google.auth.JWT(
    creds.client_email,
    null,
    creds.private_key.replace(/\\n/g, "\n"),
    ["https://www.googleapis.com/auth/spreadsheets"]
  );

  const sheets = google.sheets({ version: "v4", auth: client });

  await sheets.spreadsheets.values.update({
    spreadsheetId: process.env.SHEET_ID,
    range: "data!A1",
    valueInputOption: "RAW",
    requestBody: {
      values: values.map(row => [row])
    }
  });

  console.log("✅ Sheet updated successfully");
}
