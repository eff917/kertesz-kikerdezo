import { writable } from 'svelte/store';
let loaded = false;

export const listsData = writable({});
export const remainingPlants = writable([]);

export const fetchLists = async () => {
    if (loaded) return;
    const url = 'http://192.168.88.247:8000/api/get_lists'
    const res = await fetch(url);
    const data = await res.json();
    listsData.set(data);

    loaded = true;

}

fetchLists();