import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <nav style={styles.nav}>
        <Link to="/" style={styles.link}>Inicio</Link>
        <Link to="/categorias" style={styles.link}>Categorías</Link>
        <Link to="/vuelos" style={styles.link}>Recomendación Vuelos</Link>
        <Link to="/hoteles" style={styles.link}>Hoteles</Link>
        <Link to="/eventos" style={styles.link}>Eventos Turísticos</Link>
      </nav>

      <div style={styles.content}>
        <Routes>
          <Route path="/" element={<h1>Bienvenido a AventaTravel</h1>} />
          <Route path="/categorias" element={<Categorias />} />
          <Route path="/vuelos" element={<Vuelos />} />
          <Route path="/hoteles" element={<Hoteles />} />
          <Route path="/eventos" element={<Eventos />} />
        </Routes>
      </div>
    </Router>
  );
}

function Categorias() {
  return <h2>Página de categorías</h2>;
}

function Vuelos() {
  return <h2>Página de recomendación de vuelos</h2>;
}

function Hoteles() {
  return <h2>Página de hoteles</h2>;
}

function Eventos() {
  return <h2>Página de eventos turísticos</h2>;
}


const styles = {
  nav: {
    display: "flex",
    gap: "15px",
    padding: "10px",
    background: "#e0e0e0",
  },
  link: {
    textDecoration: "none",
    color: "black",
    fontWeight: "bold",
  },
  content: {
    padding: "20px",
  },
};

export default App;
