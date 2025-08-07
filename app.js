const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
<<<<<<< HEAD
  res.send('🚀 Hello dev from GitHub Actions Deployment!');
=======
  res.send('🚀 Hello dev from GitHub Actions Deployment!');
>>>>>>> e6adf3e (Update app.js)
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
