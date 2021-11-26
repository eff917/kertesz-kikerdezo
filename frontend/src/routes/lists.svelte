<script>
	import { listsData, remainingPlants } from '../stores/lists';
	import { plantList } from '../stores/plants';
    import { goto } from '$app/navigation';

	let listsValue;
	listsData.subscribe((values) => {
		listsValue = values;
	});
	let selectedList = 'kaszab';
	function loadList() {
		// remainingPlants.set(listsValue[selectedList])
		remainingPlants.set([...$plantList]);
        goto("/test")
	}
</script>

<h2 class="text-2xl text-center my-8 uppercase">Listák</h2>
{#each listsValue as list }
    <a class="block" href="/lists/{list.id}">{list.name}</a>
{/each}

<button
	on:click={loadList}
	class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
	>Az összes növény betöltése teszthez</button
>
