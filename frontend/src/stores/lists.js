import { writable } from 'svelte/store';
let loaded = false;

export const listsData = writable({});
export const remainingPlants = writable([]);
const listDetails = {};

export const fetchLists = async () => {
    if (loaded) return;
    const url = import.meta.env.VITE_BACKEND_ADDRESS + '/lists/all'
    const res = await fetch(url);
    const data = await res.json();
    listsData.set(data);

    loaded = true;

}

export const fetchListByID = async (id) => {
    if (listDetails[id]) return listDetails[id]

    const url = `${import.meta.env.VITE_BACKEND_ADDRESS}/lists/${id}`
    const res = await fetch(url);
    const data = await res.json();
    listDetails[id] = data;
    return data;
}

fetchLists();