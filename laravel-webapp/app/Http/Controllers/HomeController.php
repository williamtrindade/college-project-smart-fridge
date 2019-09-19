<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Repositories\ProductRepository;
use App\Repositories\TransactionRepository;

class HomeController extends Controller
{
    private $productRepository;

    public function __construct(ProductRepository $productRepository, TransactionRepository $transactionRepository)
    {
        $this->productRepository     = $productRepository;
        $this->transactionRepository = $transactionRepository;
    }

    public function index()
    {
        $productsRemovedQtt = $this->productRepository->removed()->count();
        $productsQtt        = $this->productRepository->all()->count();
        $transactionsQtt    = $this->transactionRepository->all()->count();
        return view('home')
            ->with('productsRemovedQtt', $productsRemovedQtt)
            ->with('productsQtt', $productsQtt)
            ->with('transactionsQtt', $transactionsQtt);
    }   
}
