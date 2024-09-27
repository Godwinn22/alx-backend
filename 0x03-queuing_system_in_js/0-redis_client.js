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
