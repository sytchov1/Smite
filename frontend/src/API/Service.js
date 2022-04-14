import axios from "axios";

export class Service {
    static async getItems() {
        const response = await axios.get('http://localhost:8000/api/items')
        return response;
    }

    static async getClasses() {
        const response = await axios.get('http://localhost:8000/api/classes')
        return response;
    }
}