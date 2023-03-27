import ProjectsTable from "../components/ProjectsTable";
import {useEffect, useState} from "react";
import {ProjectsApi} from "../api";

export default function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    ProjectsApi
      .getAll()
      .then(({ data }) => setProjects(data))
  }, []);

  return (
    <div>
      <ProjectsTable projects={projects}></ProjectsTable>
    </div>
  );
}
