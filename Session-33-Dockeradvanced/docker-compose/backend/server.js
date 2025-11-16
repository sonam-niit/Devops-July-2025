const express = require("express");
const mysql = require("mysql2");
const app = express();

const db= mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
})
db.connect(err =>{
    if(err) throw err;
    console.log("MYSQL Connected")
})
app.get("/", (req, res) => {
  res.send("Backend is Runnig!");
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});