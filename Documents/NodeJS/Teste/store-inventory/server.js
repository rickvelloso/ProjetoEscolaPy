const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const productRoutes = require('./routes/product');
const sequelize = require('./db/config');

const Pool = require("pg").Pool;

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  port: 5432,
  database: "postgres",
  password: "180705",
})

require('dotenv').config();

const app = express();

app.use(cors());
app.use(bodyParser.json());

app.use((req, res, next) => {
  pool.query('SELECT 1', (err) => {
    if (err) {
      console.error('Database connection error', err.stack);
      return res.status(500).json({ error: 'Database connection error' });
    }
    next();
  });
});

app.use('/products', productRoutes);

const port = process.env.PORT || 3000;

sequelize.sync()
  .then(() => {
    app.listen(port, () => {
      console.log(`Server is running on port ${port}`);
    });
  })
  .catch((error) => {
    console.error('Unable to connect to the database:', error);
  });
