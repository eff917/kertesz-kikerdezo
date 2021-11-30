<script>
	import { listsData, remainingPlants, fetchListByID } from '$lib/stores/lists';
	import { plantList } from '$lib/stores/plants';
	import { goto } from '$app/navigation';

	let listsValue;
	listsData.subscribe((values) => {
		listsValue = values;
	});
	let selectedList;
	async function loadList(listID) {
		let listToLoad = await fetchListByID(listID);
		remainingPlants.set(listToLoad.plants);
		goto('/test');
	}
</script>

<h2 class="text-2xl text-center my-8 uppercase">Listák</h2>
{#each listsValue as list}
	<a class="flex" href="/lists/{list.id}">{list.name}</a>
	<button
		on:click={loadList(list.id)}
		class="flex bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
	>
		A lista betöltése teszthez
	</button>
{/each}
