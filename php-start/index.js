const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('你好啊，你打开的是网站的首页')
})

app.listen(port, () => {
  console.log(`你现在打开的端口是： http://localhost:${port}`)
})