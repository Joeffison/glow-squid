import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';



export default function ProjectsTable({ projects }) {
  let headCells = [
    {field: 'id', label: 'ID'},
    {field: 'name', label: 'Name'},
    {field: 'number', label: 'Number'},
    {field: 'acquisition_date', label: 'Acquisition Date'},
    {field: 'number_3l_code', label: 'Number 3l code'},
    {field: 'deal_type_id', label: 'Deal Type id'},
    {field: 'group_id', label: 'Group id'},
    {field: 'status_id', label: 'Status id'},
    {field: 'company_id', label: 'Company id'},
  ];

  return (
    <TableContainer component={Paper} sx={{ maxHeight: '75vh' }}>
      <Table sx={{ minWidth: 650 }} stickyHeader aria-label="sticky table">
        <caption>Table of projects.</caption>
        <TableHead>
          <TableRow>
            {headCells.map((headCell) => (
              <TableCell
                key={headCell.field}
              >
                  {headCell.label}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {projects.map((project) => (
            <TableRow
              key={project.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              {headCells.map((headCell) => (
                <TableCell
                  key={headCell.field}
                >
                    {project[headCell.field]}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
