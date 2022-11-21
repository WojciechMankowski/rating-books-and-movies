import React from 'react';
import ReactDOM from 'react-dom/client';
import ShowItems from './Compoment/ShowItems';

const App = () => { 
  return <div className='app'>
    <h1>My App</h1>
    <ShowItems/>
  </div>
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(

    <App />
);
