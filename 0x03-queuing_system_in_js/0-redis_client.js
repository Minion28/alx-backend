import { createClient } from 'redis';

function redisConnect() {
  const cl = createClient();

  cl.on('connect', function() {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

};

redisConnect();
