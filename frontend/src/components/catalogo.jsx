import React, { useEffect, useState } from 'react';

function Catalogo() {
  const [productos, setProductos] = useState([]);
  const [categorias, setCategorias] = useState([]);

  useEffect(() => {
    // Ajusta esta URL según cómo expongas tu API (Django REST, etc.)
    fetch('/api/productos')  
      .then(res => res.json())
      .then(data => {
        setProductos(data.productos);
        setCategorias(data.categorias);
      });
  }, []);

  return (
    <div>
      <h1>Catálogo</h1>
      <select>
        <option value="">Todas las categorías</option>
        {categorias.map(c => (
          <option key={c.id} value={c.id}>{c.nombre}</option>
        ))}
      </select>
      <div>
        {productos.map(producto => (
          <div key={producto.id}>
            <h2>{producto.nombre}</h2>
            <p>Categoría: {producto.categoria.nombre}</p>
            <p>Precio: ${producto.precio}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Catalogo;
