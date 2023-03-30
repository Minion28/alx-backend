import { createClient, print } from 'redis';
import { promisify } from 'util';

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

const get = promisify(cl.get).bind(cl);

async function displaySchoolValue(schoolName) {
  const result = await get(schoolName).catch((error) => {
    if (error) {
      console.log(error);
      throw error;
    }
  });
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
