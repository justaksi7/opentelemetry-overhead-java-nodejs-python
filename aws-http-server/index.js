const express = require('express')
let requestCount = 0;
const data = {
      first_name: 'Mats',
      last_name: 'Winter',
      email: 'mats.winter@example.com',
      job: 'Backend Developer'
    };
let dataArray = [];
dataArray.push(data);
const app = express()
app.use(express.json());
const port = 3000;


app.get('/get-request', (req, res) => {
  res.send(dataArray[0]);
  requestCount++;
})

app.post('/post-request', (req, res) => {
  const newData = req.body;
  dataArray.push(newData);
  dataArray.pop();
  res.send('Data received!');
  requestCount++;
})

app.get('/request-count', (req, res) => {
  res.send({ count: requestCount });
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})