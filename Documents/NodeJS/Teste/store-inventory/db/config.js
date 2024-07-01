const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('postgres', 'postgres', '180705', {
  host: 'localhost',
  dialect: 'postgres',
});

module.exports = sequelize;
