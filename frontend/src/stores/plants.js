import { writable } from 'svelte/store';
let loaded = false;

export const plantList = writable([]);
export const plantData = writable({});
const plantDetails = {};

export const fetchPlantData = async () => {
    if (loaded) return;
    const url = import.meta.env.VITE_BACKEND_ADDRESS + '/plants/all';
    const res = await fetch(url);
    const data = await res.json();
    plantData.set(data);
    plantList.set(Object.keys(data));
    loaded = true;

};

export const fetchPlantByID = async (id) => {
    if (plantDetails[id]) return plantDetails[id]

    const url = `${import.meta.env.VITE_BACKEND_ADDRESS}/plants/${id}`
    const res = await fetch(url);
    const data = await res.json();
    plantDetails[id] = data;
    return data;
}


fetchPlantData();