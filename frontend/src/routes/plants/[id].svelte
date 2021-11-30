<script context="module">
	import { fetchPlantByID } from '../../stores/plants';

	let listsValue;
	export async function load(ctx) {
		let id = ctx.page.params.id;

		const selectedPlant = await fetchPlantByID(id);
		return { props: { selectedPlant } };
	}
</script>

<script>
	export let selectedPlant;
	console.log(selectedPlant);
</script>

<div class="flex flex-col items-center">
	<h1 class="text-4xl text-center my-8 uppercase">{selectedPlant.latin_name}</h1>
	<h2 class="text-2xl text-center my-8 uppercase">{selectedPlant.hungarian_name}</h2>
	{#each selectedPlant.pictures as picture}
		<img src={picture.path} alt="selectedPlant.latin_name" />
	{/each}
</div>
