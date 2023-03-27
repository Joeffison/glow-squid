import {useEffect, useState} from "react";

import './App.css';
import {ProjectsApi} from "./api";
import ProjectsTable from "./components/ProjectsTable";

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
        <h1>
          Wind Farm
        </h1>
      </header>
      <ProjectsTable projects={projects}></ProjectsTable>
    </div>
  );
}

export default App;
