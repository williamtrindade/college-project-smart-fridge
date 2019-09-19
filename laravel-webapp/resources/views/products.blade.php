@extends('layouts.app')
@section('content')
    <h1 style="font-size:150%;" class="mb-1 mt-4">Products in your fridge: </h1>
    <div class="shadow mt-4 p-2 rounded">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Amount</th>
                </tr>
            </thead>
            <tbody>
                @foreach($products as $product)
                    <tr>
                        <td>{{ $product->name }}</td>
                        <td>{{ $product->amount }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </div>
@endsection