// Import the Redis client library
import redis from 'redis';

// Create a Redis client instance
const client = redis.createClient();

// Handle successful connection to Redis
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (err, res) => {
		if (err) {
			console.log(err)
		}
		else {
			console.log(res)
		}
	});
};
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
