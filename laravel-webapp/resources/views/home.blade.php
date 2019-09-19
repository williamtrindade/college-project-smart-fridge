@extends('layouts.app')
@section('content')
    <h1 style="font-size:150%;" class="mb-1 mt-4">Total of products in your fridge: </h1>
    <div class="shadow mt-4 p-2 rounded">
        <h1 style="font-size:500%">
            {{ $productsQtt }}
        </h1>
    </div>
@endsection