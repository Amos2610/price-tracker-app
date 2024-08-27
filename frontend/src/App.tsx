import React, { useState, useEffect } from 'react';
import './App.css';

interface Book {
  title: string;
  price: string;
  image: string;
}

const App: React.FC = () => {
  const [books, setBooks] = useState<Book[]>([]);

  useEffect(() => {
    fetch('/books')
      .then((response) => response.json())
      .then((data) => setBooks(data))
      .catch((error) => console.error('Error fetching books:', error));
  }, []);

  return (
    <div className="ui container">
      <h1 className="ui header">Amazon Bestsellers</h1>
      <div className="ui three column grid">
        {books.map((book, index) => (
          <div key={index} className="column">
            <div className="ui card">
              <div className="image">
                <img src={book.image} alt={book.title} />
              </div>
              <div className="content">
                <div className="header">{book.title}</div>
                <div className="meta">{book.price}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
