const express = require("express");
const app = express();
const port = 5055;

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

app.get("/status", async (req, res) => {
  console.log("request received");

  await delay(4_000);

  res.status(200).json({ message: "Foo bar" });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
