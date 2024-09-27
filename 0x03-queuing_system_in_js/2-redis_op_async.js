// Import the Redis client library
import redis from 'redis';
import { promisify } from 'util';

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

// Promisify the client.get method
const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
	try {
		const data = await getAsync(schoolName);
		console.log(value)
	}
	catch (err) {
		console.log("Error: ", err)
	}
};
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
