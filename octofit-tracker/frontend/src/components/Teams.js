import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    // Copilot agent mode: Use codespace Django REST API endpoint suffix
    // Endpoint: /api/teams/
    fetch('https://automatic-telegram-v5v499jw5wwhq57-8000.app.github.dev/api/teams/')
      .then(res => res.json())
      .then(data => setTeams(data))
      .catch(err => setTeams([]));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title display-6 mb-3">Teams</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-light">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Members</th>
              </tr>
            </thead>
            <tbody>
              {Array.isArray(teams) && teams.map((team, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{team.name}</td>
                  <td>{team.members ? team.members.length : 0}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Teams;
