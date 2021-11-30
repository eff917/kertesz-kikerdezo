<script>
	import { plantData } from '../../stores/plants';

	let plantsValue;
	plantData.subscribe((values) => {
		plantsValue = values;
	});
</script>

<h2 class="text-2xl text-center my-8 uppercase">Növények</h2>
{#each plantsValue as plant}
	<p class="text-xl text-center font-bold">{plant.latin_name}</p>
	<p class="text-l text-center">{plant.hungarian_name}</p>
	<div>
		{#each plant.pictures as picture}
			<img alt={plant.latin_name} src={picture.path} />
		{/each}
	</div>
{/each}
