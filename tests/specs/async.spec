--DESCRIPTION--

Test async macros

--GIVEN--

interface AsyncInterface
{
    async public function run();
}

class AsyncClass
{
    async public function first(array $data = [])
    {
        await \Amp\File\get("path/to/file");
    }

    async public function second()
    {
        return "boo!";
    }

    async public static function complex(): string
    {

    }
}

$first = async function() {
    yield "here";
};

$second = async function() {
    $this->something();
    yield $thing;
};

$third = async () => {
    yield $thing;
};

--EXPECT--

interface AsyncInterface
{
    public function run(): \Amp\Promise;
}

class AsyncClass
{
    public function first(array $data = []): \Amp\Promise
    {
        return call_user_func(PRE_ASYNC_WRAPPER, function () {
            yield \Amp\File\get("path/to/file");
        });
    }

    public function second(): \Amp\Promise
    {
        return call_user_func(PRE_ASYNC_WRAPPER, function () {
            return "boo!";
            yield;
        });
    }

    public static function complex(): \Amp\Promise
    {
        return call_user_func(PRE_ASYNC_WRAPPER, function () {
            yield;
        });
    }
}

$first = function (): \Amp\Promise {
    return call_user_func(PRE_ASYNC_WRAPPER, function () {
        yield "here";
    });
};

$second = [$thing = $thing ?? null, "fn" => function () use (&$thing): \Amp\Promise {
    return call_user_func(PRE_ASYNC_WRAPPER, function () use (&$thing) {
        $this->something();
        yield $thing;
    });
}]["fn"];

$third = [$thing = $thing ?? null, "fn" => function () use (&$thing): \Amp\Promise {
    return call_user_func(PRE_ASYNC_WRAPPER, function () use (&$thing) {
        yield $thing;
    });
}]["fn"];
