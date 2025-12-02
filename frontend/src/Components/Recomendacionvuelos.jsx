import React, { useState } from "react";
import api from "../api/api";

function Recomendacionvuelos({ origen, destino, fechaSalida, fechaRegreso }) {
  const [recomendaciones, setRecomendaciones] = useState([]);
  const [cargando, setCargando] = useState(false);
  const [error, setError] = useState(null);
    const [mostrarRecomendaciones, setMostrarRecomendaciones] = useState(false);

    const obtenerRecomendaciones = async () => {
        setCargando(true);
        setError(null); 
        try {
            const response = await api.get("/vuelos/recomendaciones", {
                params: { origen, destino, fechaSalida, fechaRegreso },
            });
            setRecomendaciones(response.data);
        } catch (err) {
            setError("Error al obtener recomendaciones de vuelos.");
        } finally {
            setCargando(false);
        }
    };

    const manejarClick = () => {
        if (!mostrarRecomendaciones) {
            obtenerRecomendaciones();
        }
        setMostrarRecomendaciones(!mostrarRecomendaciones);
    };  
    return (
        <div>
            <button onClick={manejarClick}>
                {mostrarRecomendaciones ? "Ocultar Recomendaciones" : "Mostrar Recomendaciones"}    
            </button>
            {cargando && <p>Cargando recomendaciones...</p>}
            {error && <p>{error}</p>}
            {mostrarRecomendaciones && !cargando && !error && (     
                <ul>
                    {recomendaciones.map((vuelo) => (
                        <li key={vuelo.id}>
                            {vuelo.aerolinea} - {vuelo.numeroVuelo} - ${vuelo.precio}
                        </li>
                    ))} 
                </ul>
            )}
        </div>
    );
}
export default Recomendacionvuelos; 
