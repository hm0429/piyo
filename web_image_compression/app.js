const express = require('express')
const app = express()
app.set('view engine', 'pug')

app.get('/', (req, res) => {
	res.render('index')
})

const port = process.env.PORT || 8080
app.listen(port, () => {
  console.log('Listening on port', port)
})