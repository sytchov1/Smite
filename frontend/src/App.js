import './styles/App.css';
import { useState } from 'react';
import Header from './components/UI/header/Header';
import { BrowserRouter } from 'react-router-dom';
import AppRouter from './components/AppRouter';
import { WindowContext } from './context';
import { useWindowSize } from './hooks/useWindowSize';

function App() {
  const windowSize = useWindowSize()

  return (
    <div className="App">
      <WindowContext.Provider value={windowSize}>
        <BrowserRouter>
          <Header/>
          <AppRouter/>
        </BrowserRouter>
      </WindowContext.Provider>
    </div>
  );
}

export default App;
