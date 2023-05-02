import MenuBar from './components/MenuBar/MenuBar';
import Dashboard from './components/Dashboard/Dashboard';

import { NextUIProvider } from '@nextui-org/react';

function App() {
  return (
    <NextUIProvider>
      <MenuBar />
      <Dashboard />
    </NextUIProvider>
  );
}

export default App;
