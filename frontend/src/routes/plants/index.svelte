<script>
    import { goto } from '$app/navigation';
	import { plantData } from '../../stores/plants';

	let plantsValue;
	plantData.subscribe((values) => {
		plantsValue = values
	});
</script>

<h2 class="text-2xl text-center my-8 uppercase">Növények</h2>
{#each plantsValue as plant}
	<p>{plant.latin_name} - {plant.hungarian_name}</p>
	{#each plant.pictures as picture }
	<img alt={picture.path} src={picture.path} />
	{/each}
{/each}
