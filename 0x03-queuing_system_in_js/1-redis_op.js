import { createClient, print } from 'redis';

const cl = createClient();

cl.on('connect', function() {
  console.log('Redis client connected to the server');
});

cl.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  cl.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
  cl.get(schoolName, function(error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
