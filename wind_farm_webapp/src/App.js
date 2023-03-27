import {useEffect, useState} from "react";

import './App.css';
import {ProjectsApi} from "./api";

function App() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    ProjectsApi
      .getAll()
      .then(({ data }) => setProjects(data))
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Wind Farm
        </p>
      </header>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>
            {project.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
