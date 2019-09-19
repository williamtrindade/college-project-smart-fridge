<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Repositories\ProductRepository;

class HomeController extends Controller
{
    private $productRepository;

    public function __construct(ProductRepository $productRepository)
    {
        $this->productRepository = $productRepository;
    }

    public function index()
    {
        $productsQtt = $this->productRepository->all()->count();
        return view('home')->with('productsQtt', $productsQtt);
    }
}
