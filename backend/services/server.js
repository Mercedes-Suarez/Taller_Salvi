const express = require('express');
const cors = require('cors');  // Permite peticiones desde frontend
const app = express();
const PORT = process.env.PORT || 5000; // Mejor usar 5000 para diferenciar del frontend

app.use(cors());
app.use(express.json()); // Permite manejar JSON en las peticiones

app.get('/', (req, res) => {
  res.send('Backend funcionando correctamente');
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});

//const express = require('express');
//const app = express();
//const PORT = process.env.PORT || 3000;

//app.get('/', (req, res) => {
//  res.send('Backend funcionando correctamente');
//});

//app.listen(PORT, () => {
//  console.log(`Servidor escuchando en el puerto ${PORT}`);
//});