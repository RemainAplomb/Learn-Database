// Import the required MongoDB client library
const { MongoClient, ObjectId } = require('mongodb');

// Define the TaskManager class
class TaskManager {
    constructor() {
        // Connect to MongoDB server
        this.client = new MongoClient('mongodb://127.0.0.1:27017/');

        // Database instance
        this.db = null;
    }

    async connect() {
        try {
            // Connect to MongoDB server
            await this.client.connect();

            // Connect to the task_manager_db database
            this.db = this.client.db('task_manager_db');
            console.log('Connected to MongoDB successfully');
        } catch (error) {
            console.error('Failed to connect to MongoDB:', error);
        }
    }

    async disconnect() {
        try {
            // Disconnect from MongoDB server

            await this.client.close();
            console.log('Disconnected from MongoDB');
        } catch (error) {
            console.error('Failed to disconnect from MongoDB:', error);
        }
    }

    async addTask(collection = 'tasks', document) {
        try {
            // Insert a new task document into the specified collection
            const result = await this.db.collection(collection).insertOne(document);
            console.log('Task added successfully:', result.insertedId);
        } catch (error) {
            console.error('Failed to add task:', error);
        }
    }

    async findTasks(collection = 'tasks', condition = {}, limit = 0) {
        try {
            // Find tasks matching the specified condition in the collection
            const result = await this.db
                .collection(collection)
                .find(condition)
                .limit(limit)
                .toArray();
            console.log('Tasks found:');
            console.log(result);
        } catch (error) {
            console.error('Failed to find tasks:', error);
        }
    }

    async updateTask(collection = 'tasks', filters = {}, newValues = {}) {
        try {
            // Update the specified task with new values
            const result = await this.db.collection(collection).updateMany(filters, { $set: newValues });
            console.log('Task updated successfully:', result.modifiedCount);
        } catch (error) {
            console.error('Failed to update task:', error);
        }
    }

    async deleteTask(collection = 'tasks', filters = {}) {
        try {
            // Delete the specified task from the collection
            const result = await this.db.collection(collection).deleteMany(filters);
            console.log('Task deleted successfully:', result.deletedCount);
        } catch (error) {
            console.error('Failed to delete task:', error);
        }
    }
}

// Usage example
async function run() {
    const taskManager = new TaskManager();
    await taskManager.connect();

    // Perform operations
    const task = { title: 'Finish project', description: 'Complete the task management project', status: 'In progress' };
    await taskManager.addTask('tasks', task);
    await taskManager.findTasks('tasks');
    await taskManager.updateTask('tasks', { status: 'In progress' }, { status: 'Completed' });
    await taskManager.deleteTask('tasks', { status: 'Completed' });

    await taskManager.disconnect();
}

run();
