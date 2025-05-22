import React, { useEffect, useState } from 'react';
import { fetchMenuItems } from '../api/actions';

const Menu = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetchMenuItems()
      .then(data => setItems(data))
      .catch(console.error);
  }, []);

  return (
    <div>
      {items.map(item => (
        <>
        <div key={item.id}>
            <p>Name: {item.name}</p>
            <p>Description: {item.description}</p>
            <p>Category: {item.category}</p>
            <p>Sub Category: {item.sub_category}</p>
            <p>Cuisine: {item.cuisine}</p>
            <p>Price: ₹{item.price}</p>
            <p>Image: <img src={item.image_url} alt="Description" style={{ width: '200px' }} /></p>
        </div>
        </>
      ))}
    </div>
  );
}

export default Menu;
