@extends('layouts.app')
@section('content')
    <h1 style="font-size:150%;" class="mb-1 mt-4">Transactions of your fridge: </h1>
    <p><b>Products tha enter or out of your fridge<b></p>
    <div class="shadow mt-4 p-2 rounded">
        <table class="table">
            <thead>
                <tr>
                    <th>Product</th>
                    <th scope="col">Date</th>
                    <th scope="col">Operation Type</th>
                </tr>
            </thead>
            <tbody>
                @foreach($transactions as $transaction)
                    <tr>
                        <td>{{ $transaction->product->name   }}</td>
                        <td>{{ $transaction->datetime }}</td>
                        <td>{{ $transaction->opcode   }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </div>
@endsection