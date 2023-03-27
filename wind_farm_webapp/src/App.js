import './App.css';
import {Link, Route, Routes} from "react-router-dom";
import Home from "./pages/Home";
import Projects from "./pages/Projects";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          <Link to="/projects">Projects</Link>
        </h1>
      </header>
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/projects/" element={<Projects />} />
       </Routes>
    </div>
  );
}

export default App;
